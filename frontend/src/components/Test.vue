<template>
  <div class="test">
    <h1>{{ msg }}</h1>
    <table class="table table-bordered table-dark">
      <thead>
        <tr>
          <th scope="col">name</th>
          <th scope="col">email</th>
          <th scope="col">authenticated</th>
          <th scope="col">focus_time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in todos" :key="user.id">
          <!-- <th scope="row">{{user.id}}</th> -->
          <td>{{user.username}}</td>
          <td>{{user.email}}</td>
          <td>{{user.authenticated}}</td>
          <td>{{user.focus_time}}</td>
        </tr>
      </tbody>
    </table>
    <!--
    <table>
      <tbody>
        <tr v-for="user in todos" :key="user.id">
          <td>user id: {{user.username}}</td>
          <td>email: {{user.email}}</td>
          <td>aossword: {{user.password}}</td>
          <td>authenticated: {{user.authenticated}}</td>
          <td>focus time: {{user.focus_time}}</td>
        </tr>
      </tbody>
    </table>
    -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Test',
  data () {
    return {
      msg: 'Test Component',
      todos:null
    }
  },
  mounted(){
    //console.log('mounted')
    this.getUsers();
  },
  methods:{
    getUsers(){
      console.log('users')
      axios
        .get('http://localhost:5000/users')
        .then( response => {
          this.todos=response.data
        })
        .catch( e=> console.log(e))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.test{
  background-color: aqua;
  color:black;
}
</style>
