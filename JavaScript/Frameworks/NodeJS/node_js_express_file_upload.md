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