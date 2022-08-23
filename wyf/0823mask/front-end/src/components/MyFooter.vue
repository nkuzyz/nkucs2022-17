<template>
  <!-- 固定footer-->
  <div class="footer" :class="{ 'fixed-footer': fixed }">
    <span class="word">© 2022</span>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="less" scoped>
.fixed-footer {
    left:0;
    right: 0;
    bottom: 0;
    width: 100%;
}
.footer {
  background-color: @xTxColor;
  height: 35px;
  margin-bottom: 0;
  text-align: center;
}
.word{
    color:#fff;
    font-size: 14px;
    text-align: center;
}
</style>