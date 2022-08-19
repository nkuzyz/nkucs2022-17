<template>
  <div class="footer" :class="{ 'fixed-footer': fixed }">
  <span class="word">© 2022</span>
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
    left:0;
    right: 0;
    bottom: 0;
    width: 100%;
    z-index: 1;
}

.footer {
  background-color: @xTxColor;
  height: 35px;
  margin-bottom: 0;
  text-align: center;
  .copyright {
    a {
      color: inherit;
    }
  }
}

.word{
    color:#fff;
    font-size: 14px;
    text-align: center;

}
</style>