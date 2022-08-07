import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const MyHomePage(title: 'Contador muito legal!!'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 5;
  void showAlertDialog(BuildContext context) {
    Widget okButton = TextButton(
      child: const Text("OK"),
      onPressed: () {
        Navigator.pop(context, true);
      },
    );

    AlertDialog alert = AlertDialog(
      title: const Text("Ihuuuuul"),
      content: const Text("O contador chegou em zero."),
      actions: [
        okButton,
      ],
    );

    // show the dialog
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }

  void _decrementCounter() {
    setState(() {
      _counter--;
      if (_counter == 0) {
        showAlertDialog(context);
        _counter = 5;
      }
    });
  }
  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random(); // teste das palavras
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
        
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
            const Text(
              'vezes',
            ),
            
            // dois botões para incrementar e decrementar o contador
            ElevatedButton(
              onPressed: _incrementCounter,
              child: const Text('Incrementar'),
            ),
            ElevatedButton(
              onPressed: _decrementCounter,
              child: const Text('Decrementar'),
            ),
            
          ],
          
        ),
      ),// This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
