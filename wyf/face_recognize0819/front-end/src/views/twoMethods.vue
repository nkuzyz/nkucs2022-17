<template>
  <div>
    <!-- 顶部通栏 -->
    <AppTopNav/>

    <!-- main-->
    <div class="main">

<!--      <div class="btn1">-->
<!--        <img src="../assets/images/img5.jpg" alt=""/>-->
<!--        <Button class="bt1" @click="mtcnn">按钮1</Button>-->
<!--        <span>nihao</span>-->
<!--      </div>-->
<!--      <img class="btn1" style="padding:3% 5% 3% 5%;" src="../assets/images/img5.jpg" alt=""/>-->
<!--      <Button class="btn1" @click="mtcnn" style="padding:10% 10% 10% 10%;">按钮1</Button>-->
<!--      <span  class="btn1" >nihao</span>-->

      <div class="test1">
        <img src="../assets/images/img5.jpg" alt=""/>
        <div class="test11">
          <Button @click="mtcnn" style="margin: 0% 30% 10% 15%;">按钮1</Button>
          <span>点击体验MTCNN口罩检测</span>
        </div>
      </div>

      <div class="tableTitle"></div>

<!--      <div class="btn2">-->
<!--        <Button class="bt2" @click="yolov5">按钮2</Button>-->
<!--        <span>点击体验YOLOv5口罩检测</span>-->
<!--        <img src="../assets/images/img6.jpg" alt=""/>-->

<!--      </div>-->
      <div class="test2">
        <div class="test22">
          <Button @click="yolov5" style="margin: 10% 30% 5% 15%;">按钮2</Button>
          <span>点击体验YOLOv5口罩检测</span>
        </div>
        <img src="../assets/images/img6.jpg" alt=""/>
       </div>

    </div>
    <!-- bottom -->
    <my-footer>fixed</my-footer>
  </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import Button from '@/components/Button.vue';
import MyFooter from "@/components/MyFooter";

export default {
  name: "twoMethods",
  components: {
    MyFooter,
    AppTopNav,
    Button
  },
  methods:{
    mtcnn(){
      this.$router.replace('/homeview')
    },
    yolov5(){
      this.$router.replace('/homeview2')
    }
  }
}
</script>

<style scoped>
.test1 {
  display:flex;
}

.test1 img {
  padding:3% 5% 3% 5%;
  border-radius: 2px !important;
}

.test1 span{
  font-size: 20px;
  color:#333;
  font-weight: bold;
  width:100px;
}
.test1 .test11{
  margin:auto;
}
.test2 {
  display:flex;
}

.test2 img {
  padding:3% 5% 3% 5%;
  border-radius: 2px !important;
}

.test2 span{
  font-size: 20px;
  color:#333;
  font-weight: bold;
  width:100px;
}
.test2 .test22{
  margin:auto;
}

.main {
  /*box-sizing: border-box;*/
  width:100%;
  height:860px;
  /*display: flex;*/
  /*align-items: center;*/
}
.tableTitle {
    position: relative;
    margin:auto;
    width: 1000px;
    height: 2px;
    background-color: #d4d4d4;
    text-align: center;
    color: rgba(101, 101, 101, 1);
  }

/*.btn1{*/
/*  padding-bottom: 3%;*/
/*  padding-left: 5%;*/
/*  border-radius: 20px;*/
/*}*/
/*.bt1 img{*/
/*  border-radius: 20px;*/
/*}*/
.btn1{
  display: inline-block;
}
/*.btn2 img{*/
/*  padding-top: 3%;*/
/*  padding-left:55%;*/
/*}*/
/*.btn2 img{*/
/*  border-radius: 20px;*/
/*}*/



.bt2 {
}

</style>