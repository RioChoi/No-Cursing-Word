<script>
  import fastapi from "./lib/api"
  import Chart from './components/Chart.svelte'
  import Word from './components/Word.svelte'

  let result = "아직 뭐 없음"
  let word;
  let textValue = ''


  let items = {}

  function clearText() {
    textValue = ''
  }

  function sendText() {
    items = {
      name: "hello",
      description: textValue
    }
    fastapi('post', '/getInfo', items, (json) => {
      result = json.result
      word = json.word
    })
  }

</script>

<head>
  <title>혐오 멈춰!</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500&display=swap" rel="stylesheet">

</head>

<div class="container py-4">
  <header class="pb-3 mb-4 border-bottom">
    <a href="/" class="d-flex align-items-center text-body-emphasis text-decoration-none">
      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="32" class="me-2" viewBox="0 0 118 94" role="img"><title>Bootstrap</title><path fill-rule="evenodd" clip-rule="evenodd" d="M24.509 0c-6.733 0-11.715 5.893-11.492 12.284.214 6.14-.064 14.092-2.066 20.577C8.943 39.365 5.547 43.485 0 44.014v5.972c5.547.529 8.943 4.649 10.951 11.153 2.002 6.485 2.28 14.437 2.066 20.577C12.794 88.106 17.776 94 24.51 94H93.5c6.733 0 11.714-5.893 11.491-12.284-.214-6.14.064-14.092 2.066-20.577 2.009-6.504 5.396-10.624 10.943-11.153v-5.972c-5.547-.529-8.934-4.649-10.943-11.153-2.002-6.484-2.28-14.437-2.066-20.577C105.214 5.894 100.233 0 93.5 0H24.508zM80 57.863C80 66.663 73.436 72 62.543 72H44a2 2 0 01-2-2V24a2 2 0 012-2h18.437c9.083 0 15.044 4.92 15.044 12.474 0 5.302-4.01 10.049-9.119 10.88v.277C75.317 46.394 80 51.21 80 57.863zM60.521 28.34H49.948v14.934h8.905c6.884 0 10.68-2.772 10.68-7.727 0-4.643-3.264-7.207-9.012-7.207zM49.948 49.2v16.458H60.91c7.167 0 10.964-2.876 10.964-8.281 0-5.406-3.903-8.178-11.425-8.178H49.948z" fill="currentColor"></path></svg>
      <span class="fs-4">혐오 멈춰!</span>
    </a>
  </header>

  <div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
      단어 추가
    </button>
    <ul class="dropdown-menu">
      <form class="px-4 py-3">
        <div class="mb-3">
          <label for="exampleDropdownFormEmail1" class="form-label">욕설/혐오 단어</label>
          <input type="email" class="form-control" id="exampleDropdownFormEmail1" placeholder="욕설 입력">
        </div>
        <div class="mb-3">
          <label for="exampleDropdownFormEmail1" class="form-label">태그</label>
          <input type="email" class="form-control" id="exampleDropdownFormEmail1" placeholder="밑 표 참고">
        </div>
        <div class="mb-3">
          <label for="exampleDropdownFormEmail1" class="form-label">설명</label>
          <input type="email" class="form-control" id="exampleDropdownFormPassword1">
        </div>
        <div class="mb-3">
          <label for="exampleDropdownFormEmail1" class="form-label">용례</label>
          <input type="email" class="form-control" id="exampleDropdownFormPassword1">
        </div>
        <div class="mb-3">
          <label for="exampleDropdownFormEmail1" class="form-label">기여자 이메일</label>
          <input type="email" class="form-control" id="exampleDropdownFormPassword1" placeholder="example@example.com">
        </div>
        <div class="mb-3">
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="dropdownCheck">
            <label class="form-check-label" for="dropdownCheck">
              입력하신 내용이 전부 정확한가요?
            </label>
          </div>
        </div>
        <button type="submit" class="btn btn-primary">제출</button>
      </form>
    </ul>
  </div>

  <br>

  <div class="bg-body-tertiary p-2 mb-4 rounded">
    <div class="py-5 mx-auto">
      <div class="container">
        <div class="mb-3">
          <label for="exampleFormControlTextarea1" class="form-label">여기에 표현을 입력</label>
          <textarea class="form-control form-control-lg" id="exampleFormControlTextarea1" rows="5" type="text" bind:value="{textValue}"></textarea>
        </div>

        <button on:click={clearText}>지우기</button>
        <button on:click={sendText}>보내기</button>

      </div>
    </div>
  </div>

  <div class="row align-items-md-stretch">
    <div class="col-md-6">
      <div class="p-5 text-bg-dark rounded-3">
        <!--<p>출력값: {result}</p>-->
        <Chart {result}/>
      </div>
    </div>

    <div class="col-md-6">
      <div class="h-100 p-5 bg-body-tertiary border rounded-3" id="kk">
        <Word {word}/>
      </div>
    </div>
  </div>

  

  <div class="footer">
    <footer class="pt-3 mt-4 text-body-secondary border-top">
      © 2023 경희대학교 세계와 시민 G17분반
    </footer>
  </div>
</div>