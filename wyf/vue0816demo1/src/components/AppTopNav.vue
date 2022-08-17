<template>
    <div class="app-top-nav">
        <div class="w">
            <ul>
                <li><a href="javascript:;">
                    <i class="iconfont icon-shouyefill"></i>
                    首页
                    </a>
                </li>
                <li><a href="javascript:;">
                    <i class="iconfont icon-denglu"></i>
                    登录
                    </a>
                </li>
                <li><a href="javascript:;">
                    <i class="iconfont icon-xinrenzhinan"></i>
                    指南
                    </a>
                </li>
                <li>
                    <a href="javascript:;">
                    <i class="iconfont icon-guanyu"></i>
                    关于
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default{

}
</script>

<style lang="less" scoped>
@import url('../assets/styles/variable.less');

.app-top-nav{
    background-color:skyblue;
    ul{
        height: 53px;
        line-height: 53px;
        display: flex;
        justify-content: flex-end;
        li{
            a{
                padding: 0 10px;
                color:@xTxColor;
                border-left: 1px solid #fff;
                &:hover{
                    color: #fff;
                }
            }
        }
    }
}

</style>