# frozen_string_literal: true

input_string = nil
File.open 'inputs/day01.txt' do |puzzle_in|
  input_string = puzzle_in.read
end

# input_string = "1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"

nubmer_map = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

numbers = input_string.split("\n")
numbers = numbers.collect do |text|
  nubmer_positions = []
  nubmer_map.each do |key,value|
    ['index', 'rindex'].each do |pos|
      nubmer_positions[text.send(pos, key.to_s)] = value if text.send(pos, key.to_s)
      nubmer_positions[text.send(pos, value.to_s)] = value if text.send(pos, value.to_s)
    end
  end
  output_text = nubmer_positions.compact.first.to_s
  output_text += nubmer_positions.compact.last.to_s
  output_text
end
puts numbers.collect { |nums| nums[0] + nums[1] }.collect(&:to_i).sum
