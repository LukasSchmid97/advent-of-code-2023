# frozen_string_literal: true

input_string = nil
File.open 'inputs/day03.txt' do |puzzle_in|
  input_string = puzzle_in.read
end

# input_string = "467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."

symbol_coords = []
number_coords = [] # extending x+

num_len = ->(number) { number.to_s.size }

gear_map = {}

input_string.split("\n").each_with_index do |row, row_index|
  row.chars.each_with_index do |char, column_index|
    if /\d+/.match(char).nil? && char != '.'
      symbol_coords.push([column_index, row_index])
      if char == '*'
        gear_map[[column_index, row_index]] = []
      end
    end
  end

  cur_index = 0

  row.scan(/\d+/).each do |number|
    num_index = row[cur_index..].index(number) + cur_index
    number_coords.push([number.to_i, num_index, row_index])
    cur_index = num_index + num_len.call(number)
  end
end


relevant_numbers = number_coords.select do |number, number_x, number_y|
  keep = false
  (-1..num_len.call(number)).each do |x_mod|
    [-1, 0, 1].each do |y_mod|
      if symbol_coords.include?([number_x + x_mod, number_y + y_mod])
        keep = true
        if gear_map.key?([number_x + x_mod, number_y + y_mod])
          gear_map[[number_x + x_mod, number_y + y_mod]].push(number)
        end
      end
    end
  end
  keep
end

# puts symbol_coords.inspect
# puts number_coords.inspect
# puts relevant_numbers.inspect
# puts relevant_numbers.collect(&:first).inspect
puts relevant_numbers.collect(&:first).sum
# puts gear_map.inspect
puts gear_map.values.select { |g| g.count == 2 }.collect { |a| a.first*a.last}.sum
