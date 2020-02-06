defmodule Dictionary.Application do

  use Application

  #아래 함수를 작성하고 mix.exs에 mod필드에 등록을 해주면 아래 함수가 런타임에 자동으로 실행된다.
  def start(_type, _args) do
    #수퍼바이저라이브러리를 적용하는 방법중하나는 Application에 작성하는 것이다.
    import Supervisor.Spec

    #이 워커모듈 안에 start_link로 되어있는 함수를 실행하도록 함
    children = [
      worker(Dictionary.Words, []),
    ]

    options = [
      name: Dictionary.Supervisor,
      strategy: :one_for_one #프로세스가 죽으면 대처할때의 정책
    ]

    # 만약 child process에 버그가 있어서 프로세스가 매번 죽는다면 다시 수퍼바이저가 살리지 않도록 trial 횟수를 지정해줄수도 있다.
    Supervisor.start_link(children, options)
  end
end
