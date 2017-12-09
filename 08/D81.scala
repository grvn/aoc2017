import scala.collection.mutable.HashMap
import io.Source.fromFile
import scala.io.StdIn.readLine

object D81 {
  val registers = new HashMap[String,Int]().withDefaultValue(0)

  def main(args: Array[String]): Unit = {
    val file: String = readLine()
    val instructions: List[Instruction] = readFile(file)
    instructions.foreach(x => x.execute())
    println(registers.values.max)
  }

  def readFile(name: String): List[Instruction] = {
    val splitRegex = """^(\w+)\s+(\w+)\s+(-?\d+)\s+\w+\s+(.+)$""".r
    val input = fromFile(name)
    val instructions = input.getLines().toList.map(_ match {
      case splitRegex(target,addsub,value,tocheck) =>
        Instruction(target,addsub,value,tocheck)
    })
    input.close()
    instructions
  }

  object Instruction {
    def apply(target: String, addsub: String, value: String, tocheck: String): Instruction = {
      Instruction(target,(addsub match {case "inc" => 1 case "dec" => -1})*value.toInt,tocheck)
    }
  }

  case class Instruction(target: String, term: Int, tocheck: String){
    def execute(): Unit = tocheck.split(" ") match {
      case Array(a,">",b) => if (registers(a) > b.toInt) registers(target) += term
      case Array(a,"<",b) => if (registers(a) < b.toInt) registers(target) += term
      case Array(a,">=",b) => if (registers(a) >= b.toInt) registers(target) += term
      case Array(a,"==",b) => if (registers(a) == b.toInt) registers(target) += term
      case Array(a,"<=",b) => if (registers(a) <= b.toInt) registers(target) += term
      case Array(a,"!=",b) => if (registers(a) != b.toInt) registers(target) += term
    }
  }
}
