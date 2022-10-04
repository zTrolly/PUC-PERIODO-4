import 'package:flutter/material.dart';
import 'dart:math';

class Jogo extends StatefulWidget {
  const Jogo({super.key});

  @override
  // ignore: library_private_types_in_public_api
  _JogoState createState() => _JogoState();
}

class _JogoState extends State<Jogo> {
  var _imagemApp = const AssetImage("imagens/opcao.png");
  var _mensagem = "Escolha uma opção abaixo";

  void _opcaoSelecionada(String escolhaUsuario) {
    var opcoes = ["cara", "coroa"];
    var numero = Random().nextInt(2);
    var escolhaApp = opcoes[numero];

    switch (escolhaApp) {
      case "cara":
        setState(() {
          _imagemApp = const AssetImage("imagens/cara260.png");
        });
        break;
      case "coroa":
        setState(() {
          _imagemApp = const AssetImage("imagens/coroa260.png");
        });
        break;
    }

    if (escolhaUsuario == escolhaApp) {
      setState(() {
        _mensagem = "Você ganhou";
      });

    } else {
      _mensagem = "Você perdeu";
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Cara ou Coroa"),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          const Padding(
            padding: EdgeInsets.only(top: 32, bottom: 16),
            child: Text(
              "Escolha do Computador",
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ),
          Image(image: _imagemApp, height: 100),
          Padding(
            padding: const EdgeInsets.only(top: 32, bottom: 16),
            child: Text(
              _mensagem,
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              GestureDetector(
                onTap: () => _opcaoSelecionada("cara"),
                child: Image.asset(
                  "imagens/cara260.png",
                  height: 100,
                ),
              ),
              GestureDetector(
                onTap: () => _opcaoSelecionada("coroa"),
                child: Image.asset(
                  "imagens/coroa260.png",
                  height: 100,
                ),
              ),
            ],
          )
        ],
      ),
    );
  }
}
