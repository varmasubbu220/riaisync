from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.auth import verify_token  # Import your token verification function

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow unauthenticated routes
        public_routes = ["/auth/login", "/auth/refresh", "/docs", "/openapi.json",'/onboardusers/','/users/']
        print(request.url.path)
        if request.url.path in public_routes:
            return await call_next(request)

        # Get Authorization header
        print('logggggggggggggggg')
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing or invalid Authorization header"
            )

        # Extract token
        token = auth_header.split(" ")[1]
        payload = verify_token(token)

        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )

        # Add user info to request state
        request.state.user = payload["sub"]

        return await call_next(request)
