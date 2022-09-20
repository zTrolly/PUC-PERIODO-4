import 'package:flutter/material.dart';

// ignore: unnecessary_new
void main() => runApp(new MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.pink),
      home: MyHomePage(),
    ));

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  int numPessoas = 0;
  double precoConta = 0.0;
  double precoPorPessoa = 0.0;
  
  
  @override
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }




  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar:  AppBar(
        title:  const Text("Divide Ai!"),
      ),
      body:  Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children : <Widget> [
            OutlinedButton(onPressed: (() => print("teste")), 
            child: const Text("Divide a conta Ai!"),
            ),
            const Padding(padding: EdgeInsets.all(10.0)),
            const Text(
              "O valor total que cada um tem que pagar é de: R\$",
              style: TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
              ),
          ], 
        ),
      ),
    );
  }
}
