<template>
  <div>
    <form @submit.prevent="join">
      <input v-model="nickname" placeholder="Nickname" />
      <input v-model="room" placeholder="Room" />
      <button type="submit">Join</button>
    </form>
  </div>
</template>

<script>
import socket from '../socket'
export default { name:'ChatRoom', data(){return{nickname:'',room:''}} }
</script>
