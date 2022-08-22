<!-- <template>
  <img src="./assets/logo.png">
  <Login1/>
  <div>
    <p>
      If Element Plus is successfully added to this project, you'll see an
      <code v-text="'<el-button>'"></code>
      below
    </p>
    <el-button type="primary">el-button</el-button>
  </div>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import Login1 from './components/Login1.vue'

export default {
  name: 'App',
  components: {
    Login1
  }
}
</script>

<style>
#app{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style> -->

<template>
    <router-view/>
</template>

<style lang="less">
@import url('./assets/styles/mixins.less');
</style>
