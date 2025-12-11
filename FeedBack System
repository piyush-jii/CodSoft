import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class FeedbackManagementSystem {

    private JFrame frame;
    private JTabbedPane tabs;
    private JTextField studentField, teacherField, subjectField, dateField;
    private JTextArea commentsArea;
    private ButtonGroup clarityGroup, knowledgeGroup, communicationGroup, approachabilityGroup;
    private JTable table;
    private DefaultTableModel model;
    private final String CSV_FILE = "feedback_records.csv";

    public FeedbackManagementSystem() {
        frame = new JFrame("Feedback Management System");
        frame.setSize(1000, 650);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        tabs = new JTabbedPane();
        tabs.add("Submit Feedback", createFeedbackFormTab());
        tabs.add("View Records", createViewRecordsTab());
        frame.add(tabs);
        frame.setVisible(true);
        loadExistingFeedback();
    }

    private JPanel createFeedbackFormTab() {
        JPanel panel = new JPanel(new BorderLayout());
        JLabel title = new JLabel("Submit Feedback", SwingConstants.CENTER);
        title.setFont(new Font("SansSerif", Font.BOLD, 22));
        panel.add(title, BorderLayout.NORTH);

        JPanel form = new JPanel(new GridBagLayout());
        form.setBorder(BorderFactory.createEmptyBorder(12, 12, 12, 12));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 8, 8, 8);
        gbc.anchor = GridBagConstraints.WEST;

        gbc.gridx = 0; gbc.gridy = 0;
        form.add(new JLabel("Student Name:"), gbc);
        studentField = new JTextField(18);
        gbc.gridx = 1;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;
        form.add(studentField, gbc);

        gbc.fill = GridBagConstraints.NONE;
        gbc.weightx = 0;
        gbc.gridx = 0; gbc.gridy = 1;
        form.add(new JLabel("Teacher Name:"), gbc);
        teacherField = new JTextField(18);
        gbc.gridx = 1;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;
        form.add(teacherField, gbc);

        gbc.fill = GridBagConstraints.NONE;
        gbc.weightx = 0;
        gbc.gridx = 0; gbc.gridy = 2;
        form.add(new JLabel("Subject:"), gbc);
        subjectField = new JTextField(18);
        gbc.gridx = 1;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;
        form.add(subjectField, gbc);

        gbc.fill = GridBagConstraints.NONE;
        gbc.weightx = 0;
        gbc.gridx = 0; gbc.gridy = 3;
        form.add(new JLabel("Date (DD/MM/YYYY):"), gbc);
        dateField = new JTextField(10);
        setupAutoDateFormat(dateField);
        gbc.gridx = 1;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;
        form.add(dateField, gbc);

        gbc.fill = GridBagConstraints.NONE;
        gbc.weightx = 0;
        gbc.gridx = 0; gbc.gridy = 4;
        gbc.gridwidth = 2;
        JLabel ratingTitle = new JLabel("Rating (1–5)", SwingConstants.CENTER);
        ratingTitle.setFont(new Font("SansSerif", Font.BOLD, 16));
        form.add(ratingTitle, gbc);
        gbc.gridwidth = 1;

        clarityGroup = createRatingRow(form, "Teaching Clarity:", 5);
        knowledgeGroup = createRatingRow(form, "Subject Knowledge:", 6);
        communicationGroup = createRatingRow(form, "Communication Skills:", 7);
        approachabilityGroup = createRatingRow(form, "Approachability:", 8);

        gbc.gridx = 0; gbc.gridy = 9;
        form.add(new JLabel("Comments:"), gbc);
        gbc.gridx = 1;
        commentsArea = new JTextArea(4, 30);
        commentsArea.setLineWrap(true);
        commentsArea.setWrapStyleWord(true);
        JScrollPane scroll = new JScrollPane(commentsArea);
        scroll.setPreferredSize(new Dimension(420, 120));
        gbc.fill = GridBagConstraints.BOTH;
        gbc.weightx = 1.0;
        gbc.weighty = 0.4;
        form.add(scroll, gbc);

        gbc.fill = GridBagConstraints.NONE;
        gbc.weightx = 0;
        gbc.weighty = 0;
        gbc.gridx = 1; gbc.gridy = 10;
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 12, 0));
        JButton submitBtn = new JButton("Submit");
        JButton clearBtn = new JButton("Clear");
        submitBtn.setPreferredSize(new Dimension(120, 32));
        clearBtn.setPreferredSize(new Dimension(120, 32));
        btnPanel.add(submitBtn);
        btnPanel.add(clearBtn);
        form.add(btnPanel, gbc);

        submitBtn.addActionListener(e -> handleSubmit());
        clearBtn.addActionListener(e -> clearForm());

        panel.add(form, BorderLayout.CENTER);
        return panel;
    }

    private ButtonGroup createRatingRow(JPanel panel, String label, int rowIndex) {
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 8, 8, 8);
        gbc.anchor = GridBagConstraints.WEST;
        gbc.gridx = 0; gbc.gridy = rowIndex;
        panel.add(new JLabel(label), gbc);
        JPanel ratingPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        ButtonGroup group = new ButtonGroup();
        for (int i = 1; i <= 5; i++) {
            JRadioButton rb = new JRadioButton(String.valueOf(i));
            rb.setActionCommand(String.valueOf(i));
            group.add(rb);
            ratingPanel.add(rb);
        }
        gbc.gridx = 1; gbc.gridy = rowIndex;
        panel.add(ratingPanel, gbc);
        return group;
    }

    private JPanel createViewRecordsTab() {
        JPanel panel = new JPanel(new BorderLayout());
        JLabel title = new JLabel("Feedback Records", SwingConstants.CENTER);
        title.setFont(new Font("SansSerif", Font.BOLD, 20));
        panel.add(title, BorderLayout.NORTH);

        model = new DefaultTableModel(new String[]{
                "Student", "Teacher", "Subject", "Date",
                "Clarity", "Knowledge", "Communication",
                "Approachability", "Comments"
        }, 0);

        table = new JTable(model);
        table.setFillsViewportHeight(true);
        panel.add(new JScrollPane(table), BorderLayout.CENTER);

        JPanel bottom = new JPanel(new FlowLayout());
        JButton refresh = new JButton("Refresh");
        JButton clearAll = new JButton("Clear All Feedback");
        bottom.add(refresh);
        bottom.add(clearAll);

        refresh.addActionListener(e -> loadExistingFeedback());
        clearAll.addActionListener(e -> clearAllFeedback());

        panel.add(bottom, BorderLayout.SOUTH);
        return panel;
    }

    private void handleSubmit() {
        String student = studentField.getText().trim();
        String teacher = teacherField.getText().trim();
        String subject = subjectField.getText().trim();
        String date = dateField.getText().trim();

        if (student.isEmpty() || teacher.isEmpty() || subject.isEmpty() || date.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "Please fill all fields.");
            return;
        }
        if (clarityGroup.getSelection() == null ||
                knowledgeGroup.getSelection() == null ||
                communicationGroup.getSelection() == null ||
                approachabilityGroup.getSelection() == null) {
            JOptionPane.showMessageDialog(frame, "Please rate all criteria.");
            return;
        }
        if (!date.matches("^([0-2][0-9]|3[01])/(0[1-9]|1[0-2])/(\\d{4})$")) {
            JOptionPane.showMessageDialog(frame, "Please enter a valid date in DD/MM/YYYY format.", "Invalid Date", JOptionPane.ERROR_MESSAGE);
            return;
        }

        String clarity = clarityGroup.getSelection().getActionCommand();
        String knowledge = knowledgeGroup.getSelection().getActionCommand();
        String communication = communicationGroup.getSelection().getActionCommand();
        String approach = approachabilityGroup.getSelection().getActionCommand();
        String comments = commentsArea.getText().trim().replace(",", ";");

        saveToCSV(student, teacher, subject, date, clarity, knowledge, communication, approach, comments);
        JOptionPane.showMessageDialog(frame, "Feedback Submitted!");
        clearForm();
        loadExistingFeedback();
        tabs.setSelectedIndex(1);
    }

    private void saveToCSV(String... data) {
        boolean exists = new File(CSV_FILE).exists();
        try (PrintWriter pw = new PrintWriter(new FileWriter(CSV_FILE, true))) {
            if (!exists)
                pw.println("Student,Teacher,Subject,Date,Clarity,Knowledge,Communication,Approachability,Comments");
            pw.println(String.join(",", data));
        } catch (Exception e) {
            JOptionPane.showMessageDialog(frame, "Error writing file.");
        }
    }

    private void clearAllFeedback() {
        int confirm = JOptionPane.showConfirmDialog(
                frame,
                "Are you sure you want to delete ALL feedback records?",
                "Confirm Delete",
                JOptionPane.YES_NO_OPTION
        );
        if (confirm == JOptionPane.YES_OPTION) {
            try (PrintWriter pw = new PrintWriter(new FileWriter(CSV_FILE))) {
                pw.println("Student,Teacher,Subject,Date,Clarity,Knowledge,Communication,Approachability,Comments");
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(frame, "Error clearing file.");
            }
            loadExistingFeedback();
            JOptionPane.showMessageDialog(frame, "All feedback has been cleared.");
        }
    }

    private void loadExistingFeedback() {
        model.setRowCount(0);
        File file = new File(CSV_FILE);
        if (!file.exists()) return;

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            br.readLine();
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",", -1);
                model.addRow(parts);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(frame, "Error reading file.");
        }
    }

    private void clearForm() {
        studentField.setText("");
        teacherField.setText("");
        subjectField.setText("");
        dateField.setText("");
        commentsArea.setText("");
        clarityGroup.clearSelection();
        knowledgeGroup.clearSelection();
        communicationGroup.clearSelection();
        approachabilityGroup.clearSelection();
    }

    private void setupAutoDateFormat(JTextField dateField) {
        dateField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                String text = dateField.getText().replaceAll("[^0-9]", "");
                StringBuilder formatted = new StringBuilder();
                if (text.length() > 0) {
                    formatted.append(text.substring(0, Math.min(2, text.length())));
                    if (text.length() > 2) {
                        formatted.append("/");
                        formatted.append(text.substring(2, Math.min(4, text.length())));
                    }
                    if (text.length() > 4) {
                        formatted.append("/");
                        formatted.append(text.substring(4, Math.min(8, text.length())));
                    }
                }
                dateField.setText(formatted.toString());
                int pos = dateField.getText().length();
                dateField.setCaretPosition(pos);
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(FeedbackManagementSystem::new);
    }
}
