<template>
  <div class="footer" :class="{ 'fixed-footer': fixed }">
  <span class="word">NKCS——带资进组</span>
  </div>
</template>
<script>
export default {
  props: {
    fixed: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {};
  },
  mounted() {},
  methods: {},
};
</script>
<style lang="less" scoped>
.fixed-footer {
    position: fixed;
    left:0;
    right: 0;
    bottom: 0;
    width: 100%;
    z-index: 1;
}

.footer {
  background-color: @xTxColor;
  height: 50px;
  font-size: 14px;
  margin-bottom: 0;
  text-align: center;
  .copyright {
    a {
      color: inherit;
    }
  }
}

.word{
    margin-top: 30px;
    color:#fff;
    font-size: 20px;
    font-weight: bold;
    text-align: center;

}
</style>