<template>
  <div class="test">
    <h1>{{ msg }}</h1>
    <table>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>user id: {{user.username}}</td>
          <td>id: {{user.email}}</td>
          <td>title: {{user.password}}</td>
          <td>complete: {{user.authenticated}}</td>
          <td>title: {{user.focus_time}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Test',
  data () {
    return {
      msg: 'Test Component',
      users:null
    }
  },
  mounted(){
    this.getUsers();
  },
  methods:{
    getUsers(){
      axios
        .get('http://localhost:5000/users')
        .then( response => {
          this.users=response.data
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
