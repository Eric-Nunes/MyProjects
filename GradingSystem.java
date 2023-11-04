import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GradingSystem extends JFrame {
    private JLabel label;
    private JTextField marksField;
    private JButton calculateButton;
    private JTextArea resultArea;

    public GradingSystem() {
        setTitle("Grading System");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        label = new JLabel("Enter Marks:");
        marksField = new JTextField(10);
        calculateButton = new JButton("Calculate Grade");
        resultArea = new JTextArea(10, 30);
        resultArea.setEditable(false);

        JPanel panel = new JPanel(new FlowLayout());
        panel.add(label);
        panel.add(marksField);
        panel.add(calculateButton);

        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                calculateGrade();
            }
        });

        add(panel, BorderLayout.NORTH);
        add(new JScrollPane(resultArea), BorderLayout.CENTER);
    }

    private void calculateGrade() {
        String marksText = marksField.getText();

        try {
            double marks = Double.parseDouble(marksText);
            String grade = getGrade(marks);
            resultArea.setText("Marks: " + marks + "\nGrade: " + grade);
        } catch (NumberFormatException e) {
            resultArea.setText("Invalid input. Please enter a valid number.");
        }
    }

    private String getGrade(double marks) {
        if (marks >= 90) {
            return "A+";
        } else if (marks >= 80) {
            return "A";
        } else if (marks >= 70) {
            return "B";
        } else if (marks >= 60) {
            return "C";
        } else if (marks >= 50) {
            return "D";
        } else {
            return "F";
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                GradingSystem gradingSystem = new GradingSystem();
                gradingSystem.setVisible(true);
            }
        });
    }
}
