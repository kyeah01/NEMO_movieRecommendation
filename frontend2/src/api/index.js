import axios from 'axios'
import session from './modules/session'
import swal from 'sweetalert';

const apiUrl = '/api'

const authAxios = axios.create({
  baseURL: apiUrl,
  headers: {
    ...session.get('token'),
    'Content-Type': 'application/json',
  },
})

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params
    })
  },
  searchProfile(params) {
    if (typeof(params) === "number") {
      return authAxios.get(`/profile/${params}`)
    } else {
      return authAxios.get('/profile/', { params })
    }
  },
  signUp(profiles) {
    return axios.post(`${ apiUrl }/auth/signup/`, profiles)
      .then(res => {
        if (res.status === 201) {
          return true
        } else {
          return false
        }
      })
  },
  logIn(form) {
    const data = {
      username: form.id,
      password: form.pw
    }
    return axios.post(`${ apiUrl }/auth/`, data)
      .then(res => {
      if (res.status === 200) {
        session.set('token', { Authorization : "jwt " + res.data.token})
        authAxios.get('/profile/', {
            params : { username : data.username }
          })
          .then(res => {
            const drf = {
                "id": res.data.id,
                "username": res.data.username,
                "is_staff": res.data.is_staff,
                "profile":
                {
                  "gender": res.data.gender,
                  "age": res.data.age,
                  "Occupation": res.data.occupation
                },
                "subscription": res.data.subscription
              }
            session.set('drf', drf)
          })
        swal({
          title : data.username + "님 반갑습니다!",
          text : "로그인에 성공 하였습니다.",
          icon: "success",
          button: false,
          timer: 2000,
        });
        return data.username
      }
      else {
        swal({
          title : "아이디 혹은 비밀번호를 확인하세요.",
          text : "로그인에 실패했습니다.",
          icon: "error",
          button: false,
          timer: 2000,
          });
        return false
      }
    })
  },
  logOut() {
    return authAxios.post('/auth/logout')
      .then(res => {
        if (res.status === 200) {
          const data = session.get("drf")
          swal({
            title : data.username + "님 안녕히 가십시오!",
            text : "로그아웃에 성공 하였습니다.",
            icon: "info",
            button: false,
            timer: 2000,
          });
          session.destroy()
          return true
        } else {
          alert('error')
          return false
        }
      })
  },
  goClusterUser(data) {
    const datas =JSON.stringify({
      method: data.method,
      params: data.params
    })
    return authAxios.post('/cluster/user/', datas).then(res => {
      swal({
        title : "클러스터 완료",
        text : "아무튼 완료",
        icon: "success",
        button: false,
        timer: 2000,
      });
      return res
    })
  },
  goClusterMovie(data) {
    const datas =JSON.stringify({
      method: data.method,
      params: data.params
    })
    return authAxios.post('/cluster/movie/', datas )
      .then(res=> {
          swal({
            title : "클러스터 완료",
            text : "아무튼 완료",
            icon: "success",
            button: false,
            timer: 2000,
          });
          return res
        }
      )
  },
  goUserCustomizedRecommendation(data) {
    const datas =JSON.stringify({
      method: data.method
      })
    return axios.post(`${apiUrl}/cluster/custom`,
      datas,{
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }
    }).then(res=> {
          swal({
            title : "유서 추천 영화 알고리즘",
            text : "아무튼 완료",
            icon: "success",
            button: false,
            timer: 2000,
          });
          return res
        }
      )
  },
  patchProfileData(data) {
    const datas = JSON.stringify({
      occupation: data.occupation,
      age: data.age,
      description : data.description
    })
    return authAxios.patch('/profile/${data.id}', datas )
  },
  playSubscription(data) {
    return authAxios.post(`/subscription/${data.id}`)
        // request headers에 데이터를 json type으로 보냄
      .then(res => {
          if (res.data.data && res.status === 200) {
            session.set('drf', res.data.data)
            return true
          }
          if (res.data.status === false) {
            return false
          }
        })
    },
  newUserRating(data) {
    const datas = JSON.stringify({
      movie: data.movie,
      user: data.user,
      rating : data.rating,
      rating_date : data.rating_date
    })
    return axios.patch(`${apiUrl}/rating/`, datas, {
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }
      }).then(res => {
          if (res.status === 200) {
            return true
          }
          if (res.status !== 200) {
            return false
          }
        })
    },
}
