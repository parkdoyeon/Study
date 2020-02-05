defmodule CacheFibo.Cache do

  @fib  :fib

  def cached_fib(n) do
    lookup(n, fn ->
      cached_fib(n-2) + cached_fib(n-1)
    end)
  end

  defp lookup(n, if_not_found) do
    Agent.get(@fib, fn map -> map[n] end)
    |> complete_if_not_found(n, if_not_found)
  end

  defp complete_if_not_found(nil, n, if_not_found) do
    if_not_found.()
    |> set(n)
  end

  defp complete_if_not_found(value, _n, _if_not_found) do
    value
  end

  defp set(val, n) do
    Agent.get_and_update(@fib, fn map ->
      { val, Map.put(map, n, val)}
    end)
  end
end

