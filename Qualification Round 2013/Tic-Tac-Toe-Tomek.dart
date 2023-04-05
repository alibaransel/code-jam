import 'dart:io';

void main(List<String> args) {
  final int testCaseCount = int.parse(stdin.readLineSync() ?? "0");
  List<List<String>> cases = [];
  for (int i = 0; i < testCaseCount; i++) {
    List<String> rows = [];
    for (int j = 0; j < 4; j++) {
      String? line = stdin.readLineSync();
      rows.add(line ?? "");
    }
    stdin.readLineSync();
    cases.add(rows);
  }
  for (int i = 0; i < cases.length; i++) {
    String result = solve(cases[i]);
    print("Case #${i + 1}: $result");
  }
}

solve(List<String> rows) {
  bool containDot = false;
  for (int i = 0; i < 4; i++) {
    String row = rows[i];
    Map map = {"T": 0, "X": 0, "O": 0, ".": 0};
    for (String c in row.split("")) {
      map[c] = map[c] + 1;
    }
    if (map["T"] + map["X"] == 4) return "X won";
    if (map["T"] + map["O"] == 4) return "O won";
    if (map["."] > 0) containDot = true;
    String column = "";
    for (var j = 0; j < 4; j++) {
      column += rows[j][i];
    }
    map = {"T": 0, "X": 0, "O": 0, ".": 0};
    for (String c in column.split("")) {
      map[c] = map[c] + 1;
    }
    if (map["T"] + map["X"] == 4) return "X won";
    if (map["T"] + map["O"] == 4) return "O won";
  }
  String d = "";
  for (var i = 0; i < 4; i++) {
    d += rows[i][i];
  }
  Map map = {"T": 0, "X": 0, "O": 0, ".": 0};
  for (String c in d.split("")) {
    map[c] = map[c] + 1;
  }
  if (map["T"] + map["X"] == 4) return "X won";
  if (map["T"] + map["O"] == 4) return "O won";
  d = "";
  for (var i = 0; i < 4; i++) {
    d += rows[i][3 - i];
  }
  map = {"T": 0, "X": 0, "O": 0, ".": 0};
  for (String c in d.split("")) {
    map[c] = map[c] + 1;
  }
  if (map["T"] + map["X"] == 4) return "X won";
  if (map["T"] + map["O"] == 4) return "O won";

  if (containDot) return "Game has not completed";
  return "Draw";
}
