import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ScientificCalculator extends JFrame implements ActionListener {
    private JTextField display;
    private double num1, num2, result;
    private String operator, currentInput;

    public ScientificCalculator() {
        setTitle("Scientific Calculator");
        setSize(300, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        display = new JTextField();
        display.setHorizontalAlignment(SwingConstants.RIGHT);
        display.setEditable(false);
        add(display, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(5, 4));

        String[] buttonLabels = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "√", "+",
            "C", "=", "x²", "1/x"
        };

        for (String label : buttonLabels) {
            JButton button = new JButton(label);
            button.addActionListener(this);
            buttonPanel.add(button);
        }

        add(buttonPanel, BorderLayout.CENTER);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String actionCommand = e.getActionCommand();

        switch (actionCommand) {
            case "C":
                display.setText("");
                num1 = num2 = result = 0;
                operator = currentInput = "";
                break;

            case "=":
                num2 = Double.parseDouble(display.getText());
                performCalculation();
                currentInput = "";
                operator = "";
                break;

            case "+":
            case "-":
            case "*":
            case "/":
                if (!currentInput.isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    operator = actionCommand;
                    display.setText("");
                    currentInput = "";
                }
                break;

            case "√":
                if (!currentInput.isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    result = Math.sqrt(num1);
                    display.setText(String.valueOf(result));
                }
                break;

            case "x²":
                if (!currentInput.isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    result = num1 * num1;
                    display.setText(String.valueOf(result));
                }
                break;

            case "1/x":
                if (!currentInput.isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    if (num1 != 0) {
                        result = 1 / num1;
                        display.setText(String.valueOf(result));
                    } else {
                        display.setText("Error");
                    }
                }
                break;

            default:
                currentInput += actionCommand;
                display.setText(currentInput);
                break;
        }
    }

    private void performCalculation() {
        switch (operator) {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    display.setText("Error");
                    return;
                }
                break;
        }
        display.setText(String.valueOf(result));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ScientificCalculator calculator = new ScientificCalculator();
            calculator.setVisible(true);
        });
    }
}
