<template>
    <form class="login__box">
        <h3>{{ whataction }}</h3>
        <label v-if="signup" for="">Name</label>
        <input v-if="signup" type="text" name="name" required>
        <label for="">Email</label>
        <input type="text" name="username" required>
        <label for="">Password</label>
        <input type="text" name="password" required> 
        <div class="buttons">
            <button v-on:click="login()" v-if="signup==false" type="submit">Log In</button>
            <a v-on:click="register()" v-if="signup==false">Sign Up</a>
            <a v-on:click="login()" v-if="signup">Log In</a>
            <button v-on:click="register()" v-if="signup" type="submit">Sign Up</button>
            
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
        }
    },

    methods: {
        register(){
            if(this.signup == false){
                this.signup = true;
                this.whataction = "Sign Up";
            }
            
        },

        login(){
            if(this.signup == true){
                this.signup = false;
                this.whataction = "Sign In";
            }
        }
    }
}


</script>

<style scoped>
    .seen{

    }
</style>