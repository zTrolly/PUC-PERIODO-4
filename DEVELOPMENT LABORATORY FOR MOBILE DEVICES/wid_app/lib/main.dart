import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home:MyApp()));
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Text(
          "Texto",
          style: formataTexto(),
        ),
        ElevatedButton(onPressed: (() => {
          print("Botão clicado")
        }), child: Text("Botão"),),
      ],
    );
  }

  formataTexto() {
    return TextStyle(
      color: Colors.red,
      fontSize: 20,
      fontWeight: FontWeight.bold,
    );
  }
}
