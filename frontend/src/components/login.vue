<template>
    <form class="login__box" method="GET" @submit.prevent='handleSubmit'>
        <h3>{{ whataction }}</h3>
        <label v-if="signup" for="">Name</label>
        <input v-if="signup" type="text" name="name" required v-model="name">
        <label for="">Email</label>
        <input type="text" name="username" v-model="username" required>
        <label for="">Password</label>
        <input type="text" name="password" v-model="password" required> 

        <div class="buttons">
            <button v-if="signup==false" type="submit">Log In</button>
            <a v-on:click="register()" v-if="signup==false">Sign Up</a>
            <!-- SPLIT -->
            <a v-on:click="login()" v-if="signup">Log In</a>
            <button v-if="signup" type="submit">Sign Up</button>
            
        </div>
    </form>
</template>

<script>

const loggingIn = async (token) => {
    let reqheader = new Headers({'Authorization': "Bearer " + token});
    let request = await fetch("url", {method: 'POST', headers: reqheader});
    let status = request.then((res) => {return res.json()});
}

async function handleSubmit() {
  //...
  // Make the login API call
    console.log("User logs in");
    let form = document.querySelector(".login__box");
    let formData = new FormData(form);

    let request = await fetch(`/auth/login`, {method: 'POST', body: formData,});

    const jwt_token = request.then((response) => {return response.json()});

    localStorage.setItem("token", jwt_token);
    // Extract the JWT from the response
    // const { jwt_token } = await response.json()
    loggingIn(jwt_token);
}

export default {
    name:"login",

    data(){
        return{
            signup: false,
            whataction: "Sign In",
            typesubmit: "loginForm",
        }
    },

    methods: {
        register(){
            if(this.signup == false){
                this.signup = true;
                this.whataction = "Sign Up";
                this.typesubmit = "signUpForm";
            }
            
        },

        login(){
            if(this.signup == true){
                this.signup = false;
                this.whataction = "Sign In";
                this.typesubmit = "loginForm";
            }
        },

        // loginForm(){
        //     console.log("HEY");
        //     let name = "";
        //     let username = this.username;
        //     let password = this.password;

        //     if(this.signup == true){
        //         name = this.name;
        //     }

        //     const response = await fetch(`/auth/login`, {
        //         method: 'POST',
        //         body: JSON.stringify({ username, password }),
     
        //     })

        // },

        signUpForm(){
            console.log("HEY");
        },


    }
}


</script>
