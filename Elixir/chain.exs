defmodule Chain do

  defstruct(
    next_node: nil,
    count: 4
  )

  def start_link(next_node) do
    #spawn_link는 두번째 인자로 함수에 전달할 arg를 리스트로 받는다
    spawn_link(Chain, :message_loop, [ %Chain{ next_node: next_node } ])
    |> Process.register(:chainer)
  end

  # Chain.start_link(:"one@kakao-entui-MacBookPro") ~ four의 터미널까지 실행
  # send :chainer, {:trigger, [] }  one에서 실행
  def message_loop(%{ count: 0 }) do
    IO.puts "done" #프로세스가 더이상 chain이 없으므로 :chainer라고 부른 프로세스가 종료된다.
  end

  def message_loop(state) do
    receive do
      { :trigger, list } ->
        IO.inspect list
        :timer.sleep 500
        send { :chainer, state.next_node }, { :trigger, [ node() | list ] }
    end
    message_loop(%{ state | count: state.count-1 })
  end

end
