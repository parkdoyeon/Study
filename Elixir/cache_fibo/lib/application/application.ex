defmodule CacheFibo.Application do

  use Application

  @fib  :fib
  #아래 함수를 작성하고 mix.exs에 mod필드에 등록을 해주면 아래 함수가 런타임에 자동으로 실행된다.
  def start(_type, _args) do
    { :ok, _pid } = Agent.start_link(fn -> %{ 0 => 0, 1 => 1 } end, name: @fib)
  end
end
