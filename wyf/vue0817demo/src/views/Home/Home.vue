<template>
    <div class="home w">
        <!-- 背景图 -->
        <div class="bg">
            <div class="bg-img">
                <img src="../../assets/images/bg-img.jpg" alt="">
            </div>
            <span class="sent">动态场景下口罩佩戴监测播报与特效提醒系统:)</span>
        </div>
        <MyFooter fixed></MyFooter>
    </div>
</template>

<script>
import Button from '@/components/Button.vue';
import MyFooter from '@/components/MyFooter.vue';
export default{
    components:{
        Button,
        MyFooter
    }
}
</script>

<style lang="less" scoped>
.bg{
    // 设置背景铺满屏幕
    position: absolute;
    top: 9%;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #fff;
}
.bg-img{
    // background-color: antiquewhite;
    width:100%;
    height:100vh;
    display:table-cell;
    vertical-align: middle;
    text-align: center;
}

.sent{
    width:660px;
    position: absolute;
    top: 50%;
    left: 30%;
    transform: translate(-50%,-70%);
    color: #fff;
    font-size: 50px;
    font-weight: bold;
    text-align: center;
}

// .but{
//     margin-left: 10%;
//     margin-bottom: 50%;
//     position:relative;
// }

</style>

