<template>
  <div class='login'>
    <h1>{{ titleMsg }}</h1>
    <el-form ref="loginForm" :model="loginData" label-width="100px">
      <el-form-item label="用户名" prop="username" :rules="[{required: true, message: '用户名不能为空'}]">
        <el-input ref="username" type="password" v-model="loginData.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password" :rules="[{required: true, message: '密码不能为空'}]">
        <el-input type="password" v-model="loginData.password" autocomplete="off"></el-input>
      </el-form-item>      
      <el-form-item>
        <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
        <el-button @click="resetForm('loginForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'loginForm',
  data() {
    return {
      titleMsg: '欢迎来到旗帜世界',
      loginData: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
         if (valid) {
           console.log('submit')
         } else {
          console.log('illegad submit!!');
          return false;
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
      console.log('reset')
    }
  }
}
</script>




 
