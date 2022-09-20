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

class _MyHomePageState extends State<MyHomePage>
    with SingleTickerProviderStateMixin {
  int numPessoas = 0;
  double precoConta = 0.0;
  double precoPorPessoa = 0.0;
  double parteGarcom = 0.0;
  double porcentagem = 0.0;
  double total = 0.0;

  late Animation animation;
  late AnimationController animationController;

  @override
  void initState() {
    animationController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1000),
    );
    super.initState();
  }

  @override
  void dispose() {
    animationController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Divide Ai!"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                const Text(
                  "Preço da conta: ",
                  style: TextStyle(fontSize: 20),
                ),
                SizedBox(
                  width: 70,
                  child: TextField(
                    keyboardType: TextInputType.number,
                    onChanged: (text) {
                      setState(() {
                        precoConta = double.parse(text);
                      });
                    },
                  ),
                ),
                const Text(
                  "Quantidade de pessoas: ",
                  style: TextStyle(fontSize: 20),
                ),
                SizedBox(
                  width: 70,
                  child: TextField(
                    keyboardType: TextInputType.number,
                    onChanged: (text) {
                      setState(() {
                        numPessoas = int.parse(text);
                      });
                    },
                  ),
                ),
                const Text(
                  "Porcentagem Garçom: ",
                  style: TextStyle(fontSize: 20),
                ),
                SizedBox(
                  width: 70,
                  child: TextField(
                    keyboardType: TextInputType.number,
                    onChanged: (text) {
                      setState(() {
                        porcentagem = (double.parse(text)) / 100 * precoConta;
                      });
                    },
                  ),
                ),
              ],
            ),
            const Padding(padding: EdgeInsets.all(10.0)),
            OutlinedButton(
                onPressed: () {
                  setState(() {
                    precoPorPessoa = precoConta / numPessoas;
                    animation = Tween<double>(
                      begin: animation.value,
                      end: precoPorPessoa,
                    ).animate(CurvedAnimation(
                        curve: Curves.fastOutSlowIn,
                        parent: animationController));
                    animation.addListener(() {
                      setState(() {});
                    });
                    animationController.forward();
                    parteGarcom = (porcentagem) / 100 * precoConta;
                    total = precoPorPessoa + (parteGarcom / numPessoas);
                  });
                },
                child: const Text("Divide a conta Ai!")),
            const Padding(padding: EdgeInsets.all(10.0)),
            Text(
              "O valor total que cada um tem que pagar é de: R\$ ${animation.value.toStringAsFixed(2)}",
              style:
                  const TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
            ),
            Text(
              "A parte do garçom é de: R\$ ${parteGarcom.toStringAsFixed(2)}",
              style:
                  const TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
            ),
            Text(
              "Cada um vai ter que pagar: R\$ ${total.toStringAsFixed(2)}",
              style:
                  const TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}
