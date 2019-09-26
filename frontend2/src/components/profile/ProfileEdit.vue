<template>
    <div class="profile">
        <div class="profile-edit">
            <ul class="profile-edit__list">
                <div id="passwordChange" class="change">
                    <p>비밀번호 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 1" v-if="editToggle != 1">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 1">Close</div>
                </div>
                <div v-if="editToggle === 1" class="expand">
                    <ul>
                        <label>
                            <p>이전 비밀번호</p>
                            <input type="password" class="LoginForm__Input"  id="OLDPASSWORD" v-model="oldpassword" placeholder="이전 비밀번호" autocomplete="new-password">
                        </label>

                        <label>
                            <p>새 비밀번호</p>
                            <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPassword()}" id="PASSWORD" v-model="password" placeholder="비밀번호" autocomplete="new-password">
                            <p class="checkText" v-if="checkPassword()" >비밀번호는 최소 8글자 이상이어야 합니다.</p>
                        </label>

                        <label>
                            <p>새 비밀번호 확인</p>
                            <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPasswordConfirm()}" id="PASSWORDCONFIRM" v-model="passwordconfirm" placeholder="비밀번호 확인" autocomplete="new-password">
                            <p class="checkText" v-if="checkPasswordConfirm()" >비밀번호가 일치하지 않습니다.</p>
                        </label>
                    </ul> 
                </div>
                <div v-if="editToggle === 1" class="btn btn--primary btn--sm" :class="{'btn--disabled' : checkPasswordClear() }">변경하기</div>

                <div id="imgChange" class="change">
                    
                    <p>프로필 이미지 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 2" v-if="editToggle != 2">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 2">Close</div>
                </div>
                <div v-if="editToggle === 2" class="expand">
                    <div class="expand__img">
                        <img :src="userImg" alt="" style="width: 11vw; height: 10vw;">
                        <div  class="file-select">
                            <label>
                                <!-- We can't use a normal button element here, as it would become the target of the label. -->
                                <span class="btn btn--primary">Select File</span>
                                <!-- Now, the file input that we hide. -->
                                <input type="file" @change="changeImg"/>
                            </label>
                            <p v-if="userChangeImg">Selected File: {{userChangeImg}}</p>
                        </div>
                    </div>
                    
                </div>

                <div id="detailChange" class="change">
                    <p>개인 정보 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 3" v-if="editToggle != 3">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 3">Close</div>
                </div>
                <div v-if="editToggle === 3" class="expand">
                    <ul>
                        <div v-for="items in SignupList" :key="items.label">
                            <p class="label" :id="items.label">{{items.label}}</p>
                            <select :name="items.name" class="LoginForm__Drop" v-model="items.name">
                                <option :value="item.value" v-for="item in items.option" :key="item.value">{{item.text}}</option>
                            </select>
                        </div>
                        <label>
                            <p>한 줄 코멘트</p>
                            <input type="text" style="width:50%; min-width:480px;" :class="{LoginForm__Err : checkUserDescription()}" class="LoginForm__Input" id="USERDESCRIPTION" v-model="userDescription" placeholder="한줄 코멘트">
                            <p class="checkText" v-if="checkUserDescription()" >한 줄 코멘트는 40자를 넘을 수 없습니다.</p>
                        </label>
                        <br>
                    </ul>
                </div>
                <div v-if="editToggle === 3" class="btn btn--primary btn--sm" :class="{'btn--disabled' : checkDetailChangeClear() }">저장</div> 
            </ul>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return{
            oldpassword: '',
            password : '',
            passwordconfirm : '',
            userDescription: '',

            userImg : require('@/assets/image/defaultUserImage.jpg'),
            userChangeImg : '',

            editToggle : 0,
            editList : [
                {name: '비밀번호 변경', value: 1},
                {name: '프로필 이미지 변경', value: 2},
                {name: '개인 정보 변경', value: 3},
            ],
            SignupList : [
                { label : 'age',
                name : '',
                option: [
                    {text:  "Under 18", value : 1},
                    {text:  "18-24", value : 18},
                    {text:  "25-34", value : 25},
                    {text:  "35-44", value : 35},
                    {text:  "45-49", value : 45},
                    {text:  "50-55", value : 50},
                    {text:  "56+", value : 56},
                ]},
                { label : 'occupation',
                name : '',
                option: [
                    {text:  "other", value : 0},
                    {text:  "academic/educator", value : 1},
                    {text:  "artist", value : 2},
                    {text:  "clerical/admin", value : 3},
                    {text:  "college/grad student", value : 4},
                    {text:  "customer service", value : 5},
                    {text:  "doctor/health care", value : 6},
                    {text:  "executive/managerial", value : 7},
                    {text:  "farmer", value : 8},
                    {text:  "homemaker", value : 9},
                    {text:  "K-12 student", value : 10},
                    {text:  "lawyer", value : 11},
                    {text:  "programmer", value : 12},
                    {text:  "retired", value : 13},
                    {text:  "sales/marketing", value : 14},
                    {text:  "scientist", value : 15},
                    {text:  "self-employed", value : 16},
                    {text:  "technician/engineer", value : 17},
                    {text:  "tradesman/craftsman", value : 18},
                    {text:  "unemployed", value : 19},
                    {text:  "writer", value : 20},
                ]},
            ]
        }
    },
    methods: {
        Go() {
            this.$emit('transForm');
            window.scrollTo(0, 0);
        },
        checkPasswordClear() {
        if (this.oldpassword === ''|| this.password === '' || this.passwordconfirm === '' || this.checkPassword() || this.checkPasswordConfirm()) {
            return true
            }
        },
        checkDetailChangeClear() {
        if (this.SignupList[0].name === '' || this.SignupList[1].name === '' || this.checkUserDescription()) {
            return true
            }
        },
        checkPassword() {
            if (this.password != '' && this.password.length <= 7) {
                return true
            }
        },
        checkPasswordConfirm() {
            if (this.passwordconfirm != '' && this.passwordconfirm != this.password) {
                return true
            }
        },
        checkUserDescription() {
            if (this.userDescription != '' && this.userDescription.length > 40) {
                return true
            }
        },
        changeImg(e) {
            console.log(e)
            this.userChangeImg = e.target.files[0].name
        }
    }
}
</script>
<style lang="scss" scope>
    .btn {
        height: 2rem;
    }
</style>