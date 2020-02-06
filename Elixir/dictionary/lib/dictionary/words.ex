defmodule Dictionary.Words do

  #@me :fred #module attribute라고 함, 전역변수로 활용
  @me __MODULE__

  def start_link() do
    Agent.start_link(&word_list/0, name: @me)
  end

  def random_word() do
    #Agent.get(agent, &Enum.random/1) 파라미터로 agent를 받음
    # if :rand.uniform < 0.33 do
    #   Agent.get(@me, fn _ -> exit(:boom) end)
    # end
    Agent.get(@me, &Enum.random/1)
  end

  def word_list() do
    "../../assets/words.txt"
    |> Path.expand(__DIR__)
    |> File.read!()
    |> String.split(~r/\n/)
  end
end
