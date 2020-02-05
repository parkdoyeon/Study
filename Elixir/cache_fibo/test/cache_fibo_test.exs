defmodule CacheFiboTest do
  use ExUnit.Case
  doctest CacheFibo

  test "greets the world" do
    assert CacheFibo.hello() == :world
  end
end
