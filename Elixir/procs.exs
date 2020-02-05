defmodule Procs do
  # spawn은 독립된 프로세스를 실행한다.
  # spawn을 통해 아래 함수를 실행하면 PID가 반환된다
  # iex(15)> spawn Procs, :greeter, []
  # #PID<0.934.1>
  def greeter_one() do
    # 프로세스 아이디값을 찾고
    # iex(16)> pid = v(-1)
    # #PID<0.934.1>
    # send를 통해 해당 프로세스에 메세지를 보낸다
    # iex(17)> send pid, "world"
    # Hello "world"
    # "world"
    # 메세지를 받고 해당 블록을 수행하면 프로세스가 종료되므로,
    # send를 통해 다시 요청을 던져도 해당 블록이 수행되지 않는다.
    receive do
      msg ->
        IO.puts "Hello #{inspect msg}"
    end
    # Process.sleep(1000)
    # IO.puts "Hello #{name}"
  end

  # 재귀적으로 호출하면 게속 메세지를 receive할 수 있게 된다.
  def greeter_two(count) do
    # receive는 패턴 매칭을 통해 전달된 파라미터에 바인딩 하여 구문을 수행한다.
    # 만약 존재하지 않는 프로세스에 요청이 전달되면 해당 요청은 날아간다
    # iex(39)> send pid, "world"
    # "world"
    # 0 Hello "world"
    # iex(40)> send pid, {:add, 99}
    # 99 Hello {:add, 99}
    # {:add, 99}
    receive do
      # spawn은 독립된 프로세스를 생성하지만 spawn_link는 연결된 프로세스를 생성한다.
      # spawn_link함수를 통해 호출하면 프로세스가 종료될 때 부모 프로세스에게 영향을 준다. 프로세스 관리를 위해 일반적으로 spawn_link를 많이 사용한다.
      # iex(67)> send pid, { :boom, :bad }
      # ** (EXIT from #PID<0.104.0>) shell process exited with reason: :bad
      # bad 이유로 종료될경우 부모 프로세스넘버가 1로 바뀌면서 새로 시작됨.
      # Interactive Elixir (1.9.4) - press Ctrl+C to exit (type h() ENTER for help)
      # iex(1)> pid = spawn_link Procs, :greeter, [0]
      # #PID<0.29562.1>
      # iex(2)> send pid, "Hello"
      # 0 Hello "Hello"
      # "Hello"
      # iex(3)> send pid, { :boom, :normal }
      # {:boom, :normal}
      #
      # iex(4)> normal한 이유로 종료될경우 부모 프로세스넘버가 유지됨.
      { :boom, reason } ->
        exit(reason)
      { :add, n } ->
        greeter_two(count+n)
      :reset ->
        greeter_two(0)
      msg ->
        IO.puts "#{count} Hello #{inspect msg}"
        greeter_two(count)
    end
  end

  def greeter(count) do

  end
end
