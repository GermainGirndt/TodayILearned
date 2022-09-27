# File Upload

# Multer
```
yarn add multer
yarn add @types/multer -D
```

## Create a upload file in configs

```
import path from 'path';
import multer from 'multer';
import crypto from 'crypto';

export default {
    storage: multer.diskStorage({
        destination: path.resolve(__dirname, '..', '..', 'tmp'),
        filename(request, file, callback) {
            const fileHash = crypto.randomBytes(10).toString('hex');
            const fileName = `${fileHash}-${file.originalname}`;

            return callback(null, fileName);
        },
    }),
};
```

## Add multer - upload middleware to route

```

const upload = multer(uploadConfig);

usersRouter.patch(
    '/avatar',
    ensureAuthenticated,
    upload.single('avatar'),
    async (request, response) => {
        // logs file's metadata
        console.log(request.file);
        return response.json({ ok: true });
    },
);


```

## Final Image Upload/Update Route

```
// patch for a updating few informations

usersRouter.patch(
    '/avatar',
    ensureAuthenticated,
    upload.single('avatar'),
    async (request, response) => {
        // logs file's metadata
        try {
            const updateUserAvatar = new UpdateUserAvatarService();
            const user = await updateUserAvatar.execute({
                user_id: request.user.id,
                avatarFilename: request.file.filename,
            });

            return response.json(user);
        } catch (err) {
            return response.status(400).json({ error: err.message });
        }
    },
);
export default usersRouter;

```

## Final Image Upload/Update Service

```

import { getRepository } from 'typeorm';
import User from '../models/User';
import path from 'path';

// Node file system
import fs from 'fs';

import uploadConfig from '../config/upload';

interface Request {
    user_id: string;
    avatarFilename: string;
}

class UpdateUserAvatarService {
    public async execute({ user_id, avatarFilename }: Request): Promise<User> {
        const usersRepository = getRepository(User);

        const user = await usersRepository.findOne(user_id);

        if (!user) {
            throw new Error('Only authenticated users can change avatar.');
        }

        if (user.avatar) {
            // Delete previous avatar

            const userAvatarFilePath = path.join(
                uploadConfig.directory,
                user.avatar,
            );
            const UserAvatarFileExists = await fs.promises.stat(
                userAvatarFilePath,
            );

            if (UserAvatarFileExists) {
                await fs.promises.unlink(userAvatarFilePath);
            }
        }

        user.avatar = avatarFilename;

        await usersRepository.save(user);

        delete user.password;

        return user;
    }
}

export default UpdateUserAvatarService;

```