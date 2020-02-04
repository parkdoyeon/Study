defmodule Dictionary do
  @moduledoc """
  mix                     # on its own compiles your project
  mix run                 # runs it, and
  mix run -e ⟪code⟫       # executes the code in the context of your project
  iex -S mix              # starts iex in the context of your project—it uses mix to build the application environment and then enters iex

  inside iex:
  iex> r ModuleName       # recompiles the file containing ModuleName
  iex> c "lib/name.ex"    # compiles the given file
  """
  def hello do
    IO.puts "hello world!!asdfsd"
  end

  def random_word() do
    word_list()
    |> Enum.random()
  end

  @doc """
  OO has methods, FP has functions
  OO는 클래스 인스턴스 메소드를 사용하여 상태변경을 하게되는데, 몇가지 단점이 있다.
  1. 상태와 메소드간의 강한결합(coupling)이 발생한다. 실제세계에서는 객체지향적인 메소드 사용보다 서브클래싱을 하여 메소드를 공유하는 경우가 더 빈번하다.
  2. 역할에 대한 혼란을 야기한다. 다른 역할이 필요해질 때 클래스 확장이나 서브클래싱을 사용하는데, 이 또한 강항 결합을 야기한다.
  3. 동시성 환경에서 오브젝트의 상태값을 예기치 못하게 변형할 수 있다.

  Functions and State
  함수형 프로그래밍은 본래의 상태값을 절대 변경하지 않는다.
  상태는 변형되지 않으며, 오직 또 다른 새로운 상태를 반환할 뿐이다.
  함수는 pure하다. 즉, 함수는 쉽게 조합되거나 재사용될 수 있다.

  엘릭서의 주된 도구는 함수의 조합(파이프 오퍼레이터의 사용 등의...)이나 패턴매칭(다른 파라미터를 갖는 같은 이름의 여러의 함수를 작성하는 것)이다.
  """
  def word_list do
    "../assets/words.txt"
    |> Path.expand(__DIR__)
    |> File.read!()
    |> String.split(~r/\n/)
  end
end
