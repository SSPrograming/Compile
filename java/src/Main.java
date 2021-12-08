import org.antlr.v4.gui.TreeViewer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

import javax.swing.*;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        try {
            String source = "../input/sort.c";
            CharStream cs = CharStreams.fromFileName(source);
            CLexer lexer = new CLexer(cs);
            CommonTokenStream token = new CommonTokenStream(lexer);
            CParser parser = new CParser(token);
            ParseTree tree = parser.compilationUnit();

            // show AST in GUI
            JFrame frame = new JFrame("Antlr AST");
            JPanel panel = new JPanel();
            TreeViewer viewer = new TreeViewer(Arrays.asList(
                    parser.getRuleNames()), tree);
            panel.add(viewer);
            frame.add(panel);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.pack();
            frame.setVisible(true);
        } catch (IOException e) {
            System.err.println("无法打开文件！");
            e.printStackTrace();
        }
    }
}
