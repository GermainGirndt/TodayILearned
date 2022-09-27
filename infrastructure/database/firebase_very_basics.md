# Firebase - The Very Basics

## First Steps
**1. Create an account**  
**2. Create a new web db**   
**3. Input some values in it**  
**4. Create a project and link the .html to the db's .js**   

```
<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/7.15.0/firebase-app.js"></script>

<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/7.15.0/firebase.js"></script>

<script src="./scripts/app.js"></script>
```

**5. Configure the db in the app.js file**     

```
// Your web app's Firebase configuration
var firebaseConfig = {
apiKey: "AIzaSyDP5PWYVd0dKKJbutfNYuoJivl6BMLTwug",
authDomain: "colegio-87b4a.firebaseapp.com",
databaseURL: "https://colegio-87b4a.firebaseio.com",
projectId: "colegio-87b4a",
storageBucket: "colegio-87b4a.appspot.com",
messagingSenderId: "2618193921",
appId: "1:2618193921:web:b637412a64067125cea800",
measurementId: "G-QB0F2RZH15"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
```

**6. Enjoy your time making queries**     
```
let db = firebase.firestore();

// Get the db's items. Prints the object and the students' names.
db.collection("turmaA")
    .get()
    .then((snapshot) =>{
        snapshot.forEach((doc)=>{
            let student = doc.data()
            console.log(doc);
            console.log(student.name);
        })
    });

// Get specifically the db's item with ID E37eRixq5WLVduGsjC5j. Print the object and the student's names.
let docRef = db.collection("turmaA").doc("E37eRixq5WLVduGsjC5j")
docRef.get().then((doc) => {
    let student = doc.data()
    console.log(doc.data())
    console.log(student.name)
});
```
