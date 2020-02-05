defmodule Fibo do
  def start() do
    Agent.start_link(fn -> %{0 => 0, 1 => 1} end)
  end
  def fibo(agent, n) do
    Agent.get_and_update(agent, &(Map.get_and_update(&1, n, &(&1[n-1]+&1[n-2]))))
  end
end
