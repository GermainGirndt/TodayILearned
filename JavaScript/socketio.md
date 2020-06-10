# Socket io


### Terminal
yarn add socket.io

### Imports
```
import io from 'socket.io';
import http from 'http';
```

### main code

```

class X


	constructor() {
		this.socket()
		// dictionary for future queries by user_id
		this.connectedUsers = {}

	}
	socket() {
		// initializing
		this.io = io(this.server)

		// connecting with the client
		this.io.on('connection', socket => {
		const { user_id } = socket.handshake.query;
			this.connectedUsers[user_id] = socket.id;
			// checks if user disconected and delete user from dic
			socket.on('disconnect', () => {
				delete this.connectedUsers[user_id];
			})
		})
	}

	this.app(user(req, res, next) => {
		req.io = this.io
	})

```
