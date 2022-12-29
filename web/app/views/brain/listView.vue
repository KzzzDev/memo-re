<template>
    <div class="wrapper">
        <div class="my-pof">
            <img src="../../public/images/img001.png" alt="" class="prof-img">
            <div class="name-friend">
                <h1 class="my-name">ずんだもん</h1>
                <font-awesome-icon icon="fa-solid fa-gear" class="black-gear" inverse/>
            </div>
            <p class="m-id">Cocororororororo</p>
            <p class="m-tag">#おんなのこ #ボイスロイド</p>
        </div>
        <div class="my-list">
            <h1 class="list-h1">すべての記憶</h1>
            <button class="img-select">共有したい記憶を選択<font-awesome-icon icon="fa-regular fa-share" inverse/></button>
            <div class="img-wrapper">
                <div class="img-box">
                    <img src="../../public/images/img001.png" alt="" class="list-img">
                    <input class="img-checkbox" type="checkbox" id="img-1" checked />
                    <label for="img-1"></label>
                </div>
                <div class="img-box">
                    <img src="../../public/images/img001.png" alt="" class="list-img">
                    <input class="img-checkbox" type="checkbox" id="img-2" checked />
                    <label for="img-2"></label>
                </div>
                <div class="img-box">
                    <img src="../../public/images/img001.png" alt="" class="list-img">
                    <input class="img-checkbox" type="checkbox" id="img-3" checked />
                    <label for="img-3"></label>
                </div>
                <div class="img-box">
                    <img src="../../public/images/img001.png" alt="" class="list-img">
                    <input class="img-checkbox" type="checkbox" id="img-4" checked />
                    <label for="img-4"></label>
                </div>
                <div class="img-box">
                    <img src="../../public/images/img001.png" alt="" class="list-img">
                    <input class="img-checkbox" type="checkbox" id="img-5" checked />
                    <label for="img-5"></label>
                </div>
                <div class="img-box">
                    <img src="../../public/images/img001.png" alt="" class="list-img">
                    <input class="img-checkbox" type="checkbox" id="img-6" checked />
                    <label for="img-6"></label>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="js">

</script>

<style scoped>
*{
    font-size: 10px
}
.wrapper{
    margin-top: 50px;
    margin-left: 50px;
    margin-right: 50px;
}
.prof-img{
    width: 100px;
    height: 100px;
    border: solid 1px;
    border-radius: 100%;
    margin-right: 20px;
    float: left;
}
.name-friend{
    display: flex;
    align-items: center;
}
.my-name{
    font-size: 3.2em;
}
.black-gear{
    color: black;
    width: 28px;
    height: 28px;
    margin-left: 20px;
}
.m-id{
    font-size: 1.8em;
}
.m-tag{
    font-size: 1.4em;
}
.my-list{
    margin-top: 70px;
    clear: both;
    position: relative;
}
.list-h1{
    font-size: 22px;
    float: left;
    margin-bottom: 50px;
}
.img-select{
    font-size: 1.6em;
    color: #ffffff;
    background-color: #3D5093;
    width: 222px;
    height: 42px;
    border-radius: 10px;
    position: absolute;
    right: 0;
}
.img-wrapper{
    clear: both;
    display: flex;
    flex-wrap: wrap;
    gap: 50px;
}
.img-box{
    position: relative;
}
.list-img{
    width: 180px;
    height: 180px;
    box-shadow: black;
    border: solid 1px;
}
.img-checkbox{
    position: absolute;
    top: 12px;
    right: 12px;
}
input[type="checkbox"]{
    display: none;
}
input[type="checkbox"]+label{
    display: none;
    cursor: pointer;
    display: inline-block;
    position: relative;
    padding-left: 25px;
    padding-right: 10px;
}
input[type="checkbox"]+label::before{
    content: "";
    position: absolute;
    display: block;
    box-sizing: border-box;
    width: 24px;
    height: 24px;
    margin-top: -180px;
    margin-left: 146px;
    left: 0;
    border-radius: 50%;
    border: 2px solid;
    border-color:  #585753; /* 枠の色変更 お好きな色を */
    background-color: #fff; /* 背景の色変更 お好きな色を */
}
input[type="checkbox"]:checked+label::after{
    content: "";
    position: absolute;
    display: block;
    box-sizing: border-box;
    width: 14px;
    height: 6px;
    margin-top: -172px;
    margin-left: 148px;
    left: 3px;
    transform: rotate(-45deg);
    border-bottom: 3px solid;
    border-left: 3px solid;
    border-color:  #3C3C3C; /* チェックの色変更 お好きな色を */
}
</style>
