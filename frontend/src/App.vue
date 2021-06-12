<template>

  <!-- <img v-on:click="change()" alt="Vue logo" src="./assets/logo.png" class="logohead"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <Index/>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Index from './components/index.vue'

export default {
    name: 'App',
    components: {
    // HelloWorld
        Index
    },
    methods:{
        change(){
            console.log("You clicked");
            document.querySelector(".logohead").style.border = "solid 2px red";

        }
    }
}
</script>

<style>

*{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body, html{
    height: 100%;
    width: 100%;
}

img{
  border: solid 2px black;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
