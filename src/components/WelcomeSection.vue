<template>
  <div class="hello">
    <h1>{{ msg }} {{ username }}!</h1>  
    <h3> Measured tempurature from IOT device: </h3>
<p>{{ farenheit | temperature(true, true) }}</p>
	<h3> Statistics: </h3>
	<chart></chart>
    <button class="normal-btn exit-btn" v-on:click="doLogout">Logout</button>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
import Chart from '@/components/Chart'

export default {
  name: 'Welcome',
  components: {
    Chart
  },
  data () {
    return {
      username: '',
      farenheit: 0,
      msg: 'Welcome,'
    }
  },
  methods: {
    doLogout() {
    	this.$store.commit('updateToken', '')
    	this.$store.commit("setAuthUser",
                {authUser: '', isAuthenticated: false}
              )
    	router.push('/')
    }
  },
  mounted(){
    this.username = this.$store.state.authUser

    axios.get("/ask-current-temp")
            .then((response) => {
              this.farenheit = response.data
            })
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
.exit-btn {
	background-color: red;
}
input, .normal-btn {
  width: 200px;
}
</style>
