<template>
    <div class="indexPage">
        <nav class="login-nav">

        </nav>
        <section class="title">
            <h1>Welcome to ToDo App</h1>

            <p>Keep track of what you need to do easily! <br> Suited for work and school!</p>
        </section>
        <section class="login">
            <!-- <form class="login__box">
                <h3>SIGN IN</h3>
                <label for="">Email</label>
                <input type="text" name="username" required>
                <label for="">Password</label>
                <input type="text" name="password" required> 
                <button type="submit">Log In</button>
                <a>Register</a>
            </form> -->
            <Login/>
        </section>
    </div>
</template>

<script>
import Login from '../components/login.vue';

export default {
    name: 'index',
    components:{
        Login
    }

}
</script>

<style lang="scss">

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
    .indexPage{
        background-color: aliceblue;
        width: 100%;
        height: 100%;
        background-color: #c9e2ff;
    }

    .title{
        float: left;
        // background-color: aquamarine;
        width: 50%;
        height: 100%;
        font-family: Arial, Helvetica, sans-serif;

        & > *{
            width: 70%;
            margin: auto;
            text-align: left;
        }

        & > h1{
            font-size: 2.5rem;

            margin-top: 24vh;
        }

        & > p{
            font-size: 1.2rem;
            margin-top: 20px;
            line-height: 1.5rem;
        }
    }

    .login{
        float: right;
        // background-color: red;
        width: 50%;
        height: 100%;

        &-nav{
            height: 80px;
            position: fixed;
            background: #242424;
            width: 100%;
        }

        &__box{
            width: clamp(300px, 50%, 600px);
            background-color: white;
            margin: auto;
            height: fit-content;
            display: flex;
            flex-direction: column;
            font-family: Arial, Helvetica, sans-serif;
            padding: 35px 30px;
            border-radius: 20px;
            margin-top: 20vh;


            & > h3{
                text-align: center;
                font-size: 25px;
                font-weight: 500;
            }   

            & > label{
                margin-top: 15px;
                
                font-weight: 200;
            }

            & > input{
                border-radius: 10px;
                border: none;
                background-color: #f2f2f2;
                outline: none;
                padding: 10px 20px;
                font-size: 15px;
            }

            & > .buttons{
                display: flex;
                width: 100%;
                margin-top: 20px;
                flex-direction: row;
                justify-content: space-between;
                align-items: stretch;
                height: 40px;

                & > *{
                    width: 48%;
                    border-radius: 10px;
                    font-size: 1.3rem;
                    cursor: pointer;
                    transition: all .1s;
                    -webkit-touch-callout: none;
                    -webkit-user-select: none;
                    -khtml-user-select: none;
                    -moz-user-select: none;
                    -ms-user-select: none;
                    user-select: none;


                    &:active{
                        transform: scale(0.95);
                     
                    }
                }

                & > button{

                    background-color: #242424;
                    color: white;
                    text-align: center;
                    border: none;
                    outline: none;

                    &:hover{
                        background-color: #3d3d3d;
                    }

                    
                }

                & > a{
                    display: inline-block;
                    background-color: white;
                    color: #242424;
                    text-align: center;
                    border: solid 1px #242424;
                    line-height: 38px;

                    &:hover{
                        background-color: #ebebeb;

                    }
                }
            }




        }
    }





</style>

