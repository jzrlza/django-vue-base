<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <form class="form-signin" v-on:submit.prevent="doLogin">
      <h3>Username</h3>
      <input v-model="username" type="text" name="username"><br>
      <h3>Password</h3>
      <input v-model="password" type="password" name="password"><br><br>
      <button class="normal-btn" type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      username: '',
      password: '',
      msg: 'Welcome, Login to continue!'
    }
  },
  methods: {
    doLogin () {
      //alert(this.username)
      //alert(this.password)
      var self = this

      const input = {
        'username': this.username,
        'password' : this.password
      }
      //alert(input['name']);
      //alert(input['password']);

      axios.post('login', input).then(req =>{
        console.log(req.data)
            //alert(req.data.token);
            //self.type = req.data.type;
            
        if (req.data){
          alert('Welcome!')
          //window.location = 'sub-profile';
        } else {
          alert(req.data.message)
        }
        return req
      })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
input {
  height: 25px;
  border: 3px solid #555;
}
input:focus {
  background-color: lightblue;
}
.normal-btn {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 5px 12px;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  height: 35px;
}
input, .normal-btn {
  width: 200px;
}
</style>
