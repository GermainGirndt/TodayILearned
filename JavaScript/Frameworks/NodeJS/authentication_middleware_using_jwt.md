# Authentication Middleware

```
import { Request, Response, NextFunction } from 'express';
import { verify } from 'jsonwebtoken';

import authConfig from '../config/auth';

interface TokenPayload {
    iat: number;
    exp: number;
    sub: string;
}

export default function ensureAuthenticated(
    request: Request,
    response: Response,
    next: NextFunction,
): void {
    // token jwt validation () - header name = authorization
    const authHeader = request.headers.authorization;

    if (!authHeader) {
        throw new Error('JWT token is missing');
    }

    // token format: 'Bearer XXXXXXXX' = type + token
    // we're not using type
    const [type, token] = authHeader.split(' ');

    try {
        const decoded = verify(token, authConfig.jwt.secret);

        const { sub } = decoded as TokenPayload;

        request.user = {
            id: sub,
        };
        console.log(decoded);

        return next();
    } catch (err) {
        throw new Error('Invalid JWT token');
    }
}

```