# Not Found: /favicon.ico

### Error

"GET /static/favicon.ico HTTP/1.1" 404 1659
Not Found: /favicon.ico



### 127.0.0.1:8000 vs localhost:8000의 차이?

127.0.0.1:8000으로 접속했을때 해당 에러가 발생했는데, localhost로 바꾸니 사라졌다. 이 둘의 차이가 뭐길래?

http://blog.naver.com/PostView.nhn?blogId=tajo70&logNo=100202261837

[내부접속localhost와-외부접속의-의미](https://prometheus.tistory.com/entry/내부접속localhost와-외부접속의-의미)

* localhost는 **loopback** 예약어다. 

  > **loopback** 
  >
  > * 신호또는 데이터의 지나온 경로가 되돌려지는 것/  자신에게 데이터를 송신하는 것이나 그와 같은 기능. 네트워크 카드에는 자신을 가르키는 「loopback address」가 설정되어 있어 이 주소에 송신된 데이터는 카드내에 수신쪽에 수신되어진다. 기기가 정상으로 가동하고 있는지 아닌지를 확인하기 위해 시험삼아 데이터를 보낼떼 사용한다. 이런 것을 loopback device라고 한다.
  >
  > https://wwwi.tistory.com/22



짧게 말해 OS에서 제공해주는 자동 loopback 호스트 네임이라는건데 favicon Error에 대해서는 정확하게 찾지 못했따. ..

