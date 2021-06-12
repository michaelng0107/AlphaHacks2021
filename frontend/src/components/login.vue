<template>
    <form class="login__box" method="GET" @submit.prevent='loginForm'>
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

        loginForm(){
            console.log("HEY");
        },

        signUpForm(){
            console.log("HEY");
        },


    }
}


</script>
