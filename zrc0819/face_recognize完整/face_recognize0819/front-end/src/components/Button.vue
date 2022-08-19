<template>
<!--  <button class="button ellipsis" :class="[size, type]">-->
<!--    <slot />-->
<!--  </button>-->
  <div
  @mousemove="onMousemove"
  :style="{ backgroundColor: `hsl(${x}, 80%, 50%)` }"
  class="movearea"
>
<!--  <p>Move your mouse across this div...</p>-->
<!--  <p>x: {{ x }}</p>-->
</div>
</template>
<script>
// export default {
//   name: 'MyButton',
//   props: {
//     size: {
//       type: String,
//       default: 'middle'
//     },
//     type: {
//       type: String,
//       default: 'default'
//     }
//   }
// }
export default {
  data() {
    return {
      x: 0
    }
  },
  methods: {
    onMousemove(e) {
      this.x = e.clientX
    }
  }
}

</script>
<style scoped lang="less">
.movearea {
  text-align: center;
  width:198px;
  height:50px;
  border-radius: 10px;
  transition: 0.3s background-color ease;
}
.my-button {
  margin-right: 5px;
  appearance: none;
  border: none;
  outline: none;
  text-align: center;
  border: 1px solid transparent;
  border-radius: 4px;
  cursor: pointer;
}
.ellipsis {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
.large {
  width: 240px;
  height: 50px;
  font-size: 16px;
}
.middle {
  width: 180px;
  height: 50px;
  font-size: 16px;
}
.small {
  width: 100px;
  height: 32px;
  font-size: 14px;
}
.mini {
  width: 60px;
  height: 32px;
  font-size: 14px;
}
.default {
  border-color: #e4e4e4;
  color: #666;
}
.primary {
  border-color: #27ba9b;
  background: #27ba9b;
  color: #fff;
}
.plain {
  border-color: #27ba9b;
  color: #27ba9b;
  background: lighten(#27ba9b, 50%);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  border-radius: 5px;
}
.gray {
  border-color: #ccc;
  background: #ccc;
  color: #fff;
}
</style>

