<template>
    <div id="main-container">
        <LeftMenu v-if="showLeftMenu"
                  :style="{width: leftWidth}"
                  @menuChange="menuChange"
                  @colChange="colChange"
                  :menu-list="menuList"></LeftMenu>
        <div :class="{'full-width':!showLeftMenu,'col-left':colState}" style="width: calc(100% - 216px);">
            <div class="top-menu" v-if="showLeftMenu&&IsFarme">
                <span>{{coMenu}}</span><span style=" font-weight: bold;">{{nowTitle}}</span>
            </div>
            <router-view
                :class="{'router-style':true,'content-body':showLeftMenu&&IsFarme,'farme-style':!IsFarme}"/>
        </div>
    </div>
</template>

<script>
    // import LeftMenu from '@/components/base/leftMenu'
    import LeftMenu from '@/components/base/eleLeft.vue'
    import {frameRouter} from '@/router/frameRouter.js'

    export default {
        name: 'main-container',
        props: {
            menuList: {}
        },
        components: {
            LeftMenu
        },
        data() {
            return {
                showLeftMenu: true,
                coMenu: '',
                IsFarme: true,
                appType: '',
                headerHeight: '60px',
                leftWidth: '65px',
                nowTitle: '',
                colState: false
            }
        },
        created() {
            this.isShowLeftMenu();
            this.judgeFarme()
        },
        methods: {
            judgeFarme() {
                for (let item in frameRouter) {
                    if (this.$route.name === frameRouter[item].name) {
                        this.IsFarme = false
                    }
                    if (this.$route.name === 'InstancePage') {
                        this.IsFarme = true
                    }
                }
            },
            isShowLeftMenu() {
                if (this.$route.path === '/' || this.$route.path === '/home') {
                    this.showLeftMenu = false;
                    this.colChange(false)
                } else {
                    this.showLeftMenu = true;
                }
            },
            menuChange(data) {
                this.coMenu = ''
                this.nowTitle = ''
                let titleDatas = data.split('>')
                for (let item in titleDatas) {
                    if (parseInt(item) + 1 !== titleDatas.length) {
                        this.coMenu += titleDatas[item] + ' > '
                    } else {
                        this.nowTitle = titleDatas[item]
                    }
                }
            },
            colChange(data) {
                if (this.showLeftMenu) {
                    this.colState = data
                    this.leftWidth = data ? '64px' : '216px'
                } else {
                    this.colState = false
                }
            }
        },
        watch: {
            $route: function () {
                this.judgeFarme()
                this.isShowLeftMenu()
            }
        },
    }
</script>

<style lang="scss" scoped>
    $headerHeight: 60px;
    #main-container {
        width: 100%;
        background: #fff;
        @media (max-width: 1920px) {
            top: 60px !important;
        }
        @media (min-width: 1920px) {
            top: 64px !important;
        }
        position: absolute;
        display: flex;
        overflow: hidden;

        .full-width {
            width: 100% !important;
        }

        .col-left {
            width: calc(100% - 64px) !important;
        }

        .router-style {
            background-color: #ffffff;
            height: calc(100% - 30px) !important;
            color: $font-second;
        }

        .farme-style {
            padding: 16px !important;
        }

        .content-body {
            height: calc(100% - 30px) !important;
            width: calc(100%) !important;;
            padding: 0px 16px 16px 16px;
            background-color: $background-color;
        }

        .top-menu {
            height: 32px;
            background-color: $background-color;
            font-size: 14px;
            line-height: 32px;
            padding-left: 16px;
            vertical-align: bottom;
        }
    }
</style>
